class Job:
    def __init__(self, id, deadline, profit):
        self.id = id            # Job ID
        self.deadline = deadline # Job deadline
        self.profit = profit     # Job profit
def jobScheduling(jobs):
    # Sort jobs based on profit in descending order
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Find maximum deadline to determine the size of slots array
    max_deadline = max(job.deadline for job in jobs)

    # Array to track which slots are filled. Initialize to -1 (empty slots).
    slots = [-1] * (max_deadline + 1)

    # List to store the jobs that will be scheduled
    scheduled_jobs = []

    # Process each job
    for job in jobs:
        # Find a free slot for this job (starting from the job's deadline)
        for t in range(job.deadline, 0, -1):
            if slots[t] == -1:  # Slot is empty
                slots[t] = job.id  # Assign job to this slot
                scheduled_jobs.append(job)  # Add job to the scheduled list
                break

    return scheduled_jobs
if __name__ == "__main__":
    # Sample jobs: Job(id, deadline, profit)
    jobs = [
        Job(1, 4, 20),
        Job(2, 1, 10),
        Job(3, 1, 40),
        Job(4, 1, 30),
        Job(5, 3, 50)
    ]
    
    # Get the list of scheduled jobs
    result = jobScheduling(jobs)

    # Display the result
    print("Scheduled Jobs (ID):")
    for job in result:
        print(f"Job ID: {job.id}, Deadline: {job.deadline}, Profit: {job.profit}")
