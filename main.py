
import psutil

class MyTask:

    @classmethod
    def mem_prof_cpu(cls):
        """Memory Profiler for CPU"""
        process=psutil.Process()
        cpu_mem =process.memory_info().rss
        mem_used_by_task = round((cpu_mem)/(1024*1024))
        percent_mem_usage = process.memory_percent()
        return mem_used_by_task,percent_mem_usage
    
def normal_function():
    result,percent = MyTask.mem_prof_cpu()
    print(result,percent*100)

if __name__ == '__main__':
    normal_function()

