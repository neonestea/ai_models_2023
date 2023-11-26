docker exec kafka kafka-console-producer --version

docker exec -it cli-tools kafka-consumer-groups --bootstrap-server broker0:29092 --describe --group people.adv.python.grp-0
