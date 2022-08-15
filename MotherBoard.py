class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr
class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume
class MotherBoard:
    def __init__(self, name, cpu, mem_slots):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mem_slots[:self.total_mem_slots]
    def get_config(self):
        mem_lst = "; ".join([f"{i.name} - {i.volume}" for i in self.mem_slots])
        # print(self.mem_slots)
        return [f'Материнская плата: {self.name}',
f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
f'Слотов памяти: {self.total_mem_slots}',
f'Память: {mem_lst}']

cpu = CPU('Intel', 2000)
mem1, mem2 = Memory('Kingstone', 4000), Memory('Kingstone', 4000)
mb = MotherBoard('Asus', cpu, [mem1, mem2])
#print(mb.get_config())
