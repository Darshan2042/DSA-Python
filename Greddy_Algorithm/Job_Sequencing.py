def job_sequencing(jobs):
    jobs.sort(reverse = True)

    max_deadline = max(job[1] for job in jobs)
    slot = [0] * (max_deadline + 1)
    total_profit = 0
    count_jobs = 0
    for profit , deadline , id in jobs:
        for j in range(deadline , 0 , -1):
            if slot[j]==0:
                slot[j] = id
                total_profit += profit
                count_jobs += 1
                break
    return count_jobs  ,total_profit

jobs = [(100,2,'J1'),(19,1,'J2'),(27,2,'J3'),(25,1,'J4'),(15,3,'J5')]
print(job_sequencing(jobs))