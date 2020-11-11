import numpy as np
import pandas as pd
import random
import time

class ProbabilisticSampling:
    def build_equiv_rel(self, datas, fd, attrSet):
        epsilon = {}
        for attr in attrSet:
            epsilon[attr] = {}

        #work on left fd
        for i in fds[:, 0]:
            dict = {}
            attData = datas[:,i]
            for j, d in enumerate(attData):
                if not dict:
                    dict[d] = {j}
                else:
                    if d not in dict:
                        dict[d] = {j}
                    else:
                        dict[d].add(j)
            epsilon[i] = dict

        #work on right fd
        fdRight = set()
        for (left, right) in fds:
            fdRight.add(right)
            dict = {}
            for val in epsilon[left]:
                if val and val != -1:
                    key = "v" + str(left) + str(val)
                    if len(epsilon[left][val]) > 0:
                        for idx in epsilon[left][val]:
                            if not dict:
                                dict[key] = {idx}
                            else:
                                if key not in dict:
                                    dict[key] = {idx}
                                else:
                                    dict[key].add(idx)
                    if dict:
                        if key not in epsilon[right]:
                            epsilon[right][key] = dict[key]

        tmplist = []
        right_dict = {}
        for r in fdRight:
            arr = epsilon[r].values()
            arr = list(arr)
            for i in range(len(arr)-1):
                for j in range(1, len(arr)):
                    if i == j:
                        continue
                    if arr[j] and any(val in arr[i] for val in arr[j] if arr[i]):
                        arr[i] |= set(arr[j])
                        arr[j] = None

            combined_eq_rel_indices = [a for a in arr if a is not None]

            sequential_no = 0
            for i, each_set in enumerate(combined_eq_rel_indices):
                realvalue = datas[random.sample(each_set, 1)[0]][r]
                use_real_value = True
                for row_index in each_set:
                    if realvalue != datas[row_index][r]:
                        use_real_value = False
                        break

                key = ""

                if use_real_value and realvalue != None:
                    key = realvalue
                else:
                    key = "v" + str(sequential_no)
                    sequential_no += 1

                right_dict[key] = each_set
            epsilon[r] = right_dict
            right_dict = {}
        return epsilon

    def is_clean(self, instance, epsilon):
        clean = True
        for attr in epsilon:
            if 'v0' in epsilon[attr] and len(epsilon[attr]['v0']) > 1:
                expected_value = None
                for row in epsilon[attr]['v0']:
                    if instance[row][attr] != None:
                        if expected_value == None:
                            expected_value = instance[row][attr]
                        elif expected_value != instance[row][attr]:
                            return False
        return clean

    def gen_repair(self, instance, fds, attrSet):
        cleancells = np.full([len(instance), len(instance[0])], None)

        no_of_val = 1

    #     Generate set indices
        index_set = set()
        for i in range(len(instance)):
            for j in range(1, len(instance[0])):
                index_set.add((i, j))
        prevepsilon = {}
        while None in cleancells and index_set:
            row, col = random.sample(index_set, 1)[0]
            index_set.remove((row, col))
            cleancells[row][col] = instance[row][col]
            epsilon = self.build_equiv_rel(cleancells, fds, attrSet)
            isclean = self.is_clean(cleancells, epsilon)
            if not isclean:
                belonged_key = None
                expected_values = set()
                for key, value in prevepsilon[col].items():
                    if row in value:
                        belonged_key = key
                        value.remove(row)
                        while None in value:
                            value.remove(None)
                        expected_values = value
                        break

                if belonged_key == None:
                    cleancells[row][col] = 'var' + str(no_of_val)
                    no_of_val += 1
                elif belonged_key == 'v0':
                    if len(expected_values) >= 1:
                        cleancells[row][col] = cleancells[expected_values.pop()][col]
                    else:
                        cleancells[row][col] = 'var' + str(no_of_val)
                        no_of_val += 1

            prevepsilon = epsilon

            cleancells_with_tuplieid = np.concatenate((instance[:,:1], cleancells[:,1:]), axis=1)
        return cleancells_with_tuplieid

    def get_multiple_repairs(self, datas, fds, no_of_instances):
        r_instances =  np.expand_dims(self.gen_repair(datas, fds, range(len(datas[0]))), axis=0)
        for i in range(1,no_of_instances):
            repair = self.gen_repair(datas, fds, range(len(datas[0])))
            r_instances = np.concatenate((r_instances, [repair]), axis=0)
        return r_instances

    def sample_tuple_from_repair_instances(self, tupleid, no_of_samples, r_instances):
        sample_tuples = np.expand_dims(r_instances[np.random.randint(len(r_instances))][tupleid], axis=0)
        for i in range(1, no_of_samples):
            sample_tuple = r_instances[np.random.randint(len(r_instances))][tupleid]
            sample_tuples = np.concatenate((sample_tuples, [sample_tuple]), axis=0)
        return sample_tuples

    def calc_prob(self, samples):
        dicts = {}
        for x in samples:
            if x in samples:
                index = -1
                for i, val in enumerate(samples):
                    if np.all(samples[i]==x):
                        index = i
                        break

                if index not in dicts:
                    dicts[index] = 1
                else:
                    dicts[index] += 1

        output = []
        n = len(samples)
        for key in dicts:
            amount = dicts[key]
            new_tuple = np.concatenate((samples[key], [amount/n]), axis=0)
            if len(output) == 0:
                output = np.expand_dims(new_tuple, axis=0)
            else:
                output = np.concatenate((output, [new_tuple]), axis=0)
        return output

    def get_probabilistic_samples(self, raw_data, fds, no_of_instances, no_of_samples):
        repair_instances = self.get_multiple_repairs(raw_data, fds, no_of_instances)
        samples = []
        for tuple_id in np.squeeze(raw_data[:, :1], axis=1):
            sample_tups = self.sample_tuple_from_repair_instances(tuple_id-1, no_of_samples, repair_instances)
            sample_tups_with_prob = self.calc_prob(sample_tups)
            if len(samples) == 0:
                samples = sample_tups_with_prob
            else:
                samples = np.concatenate((samples, sample_tups_with_prob), axis=0)
        return samples

data_from_file = pd.read_csv("RandomData500x8.csv", header=None).to_numpy()
ori_instance = data_from_file
# ori_instance= np.array([[1,14,59,90,64,55,6,88]
# ,[2,14,19,21,64,93,69,96]
# ,[3,98,64,20,64,90,53,27]
# ,[4,14,73,3,98,8,92,7]
# ,[5,73,25,90,64,58,66,99]
# ,[6,14,53,90,64,12,81,9]
# ,[7,66,66,62,18,88,53,11]])
fds = np.array([[1, 2], [4, 5]])
ps = ProbabilisticSampling()
# result = ps.gen_repair(ori_instance, fds, range(len(ori_instance[0])))
# print(result)
no_of_instances = 10 #number of repair instances that we want to generate
no_of_samples = 20 #number of samples used to calculate the probability
start = time.time()
probabilistic_samples = ps.get_probabilistic_samples(ori_instance, fds, no_of_instances, no_of_samples)
print("running time:", time.time() - start)
np.savetxt("probabilistic_samples.csv", probabilistic_samples, delimiter=",", fmt='%s')
