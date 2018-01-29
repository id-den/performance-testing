# Load Testing

**Load Testing** is type of performance testing to check system with constantly increasing the load on the system until the time load is reaches to its threshold value. Here Increasing load means increasing number of concurrent users, transactions & check the behavior of application under test. It is normally carried out underneath controlled environment in order to distinguish between two different systems.


- Taurus: bzt <name_file>.yml -report
- Locust: locust -f <name_file>.py --host=https://performance-testing.jimdo.com
    * Web monitor at *:8089