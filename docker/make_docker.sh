echo "unwrapping a docker image and starting a conatiner"
docker build -t docker_ansible .
wait
# run the docker container in background 
docker run -dit --name ansi-docker  docker_ansible 
docker_cont=`docker ps | grep 'docker_ansible' | awk '{print $1}'`
echo $docker_cont 
docker cp hosts  "$docker_cont":/.
docker cp docker.yml "$docker_cont":/.
docker cp ansible.cfg "$docker_cont":/.
docker cp ~/.ssh/id_rsa "$docker_cont":/tmp/.
docker cp ~/.ssh/id_rsa.pub "$docker_cont":/tmp/.
#docker exec $docker_cont ansible-playbook /docker.yml
#if $1 = clean
#docker rm $(docker ps -a -q) 
