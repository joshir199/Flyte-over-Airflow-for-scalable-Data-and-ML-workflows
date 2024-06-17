# Flyte-over-Airflow-for-scalable-Data-and-ML-workflows
Understanding advantages of using Flyte over Apache Airflow for scalable Data and ML pipeline solutions 

***************************
# Airflow
It is a workflow orchestration platform for orchestrating distributed applications developed by Airbnb. It leverages DAGs (Directed Acyclic Graphs) to schedule jobs across several servers or nodes.
It is also used to manage Data Pipelines.

Even though Airflow is known to be commonly used for ETL/ELT tasks but by design it is basically a Job Scheduler. It is not designed for scaling to very high scale.

Limitation:
1.  There is no built-in capability to limit resource usage on a per-task basis, and workers are not isolated from user code. Thus, It does not follows isolation principle of system design.
2.  Not favorable for highly scaling architecture.
3.  When it comes to transferring or retrieving data from cloud storage in Airflow, the process typically involves using an operator.
4.  They are not built with strong types for inputs and outputs between tasks. This makes it more susceptible to failures.
5.  It only supports Python language which makes least flexible in tech world.

**************************
# Flyte
The infinitely scalable and flexible workflow orchestration platform that seamlessly unifies data, ML and analytics stacks. It uses tasks and workflows running with the help Job Schedulers.
It captures and resolves all the limitations posed by older softwares like Airflow.

Advantages : 
1. It has built-in use custom resource usage per task basis and thus helps in managing the resources very well.
2. Versioning becomes integral part of the Flyte platform, allowing different teams to experiment on a centralised architecture. 
3. It can help in ETL/ELT as well as various others ML pipelines, thus enables different types of workloads together.
4. Strongly typed inputs and outputs can simplify data validation and highlight incompatibilities between tasks making it easier to identify and troubleshoot errors before launching the workflow.
5. Recovery capability requires Rerun only failed tasks in a workflow to save time, resources, and more easily debug.

Moreover, Flyte offers a significant advantage in terms of environment and dependency isolation. 
Code and libraries are packaged within Docker images, enabling the use of different libraries and versions per team or even for specific tasks.

Additionally, Flyte organizes projects into logical domains, such as development, staging, and production. 
These domains facilitate a step-by-step promotion of code to production ensuring adherence to best development practices like CI/CD, unit/integration testing, and code review. 

With Flyte’s environment isolation, teams can maintain control over their dependencies and ensure reproducibility while adhering to robust software engineering practices throughout the project lifecycle.

