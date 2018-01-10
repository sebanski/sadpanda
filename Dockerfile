FROM centos
MAINTAINER alex.balzer <zabbal22@gmail.com>

# TODO: debug this container

COPY . /opt/sadpanda

COPY keygen.py /etc/sadpanda.d/keygen.py
RUN /usr/bin/python /etc/sadpanda.d/keygen.py --num-chars=257654 >> /etc/sadpanda.d/poppyfarms.ve && \
	/usr/bin/python /etc/sadpanda.d/keygen.py --num-chars=257654 >> /opt/sadpanda/blockchain.evk && \
	yum -y install epel-release && \
  yum -y install libsnappy gcc python34 python34-devel python34-setuptools gcc-c++ libsnappy-devel snappy-devel && \
  easy_install-3.4 pip && \
	#yum -y install python-pip libsnappy && \
	pip3 install virtualenv pytest && \
	virtualenv /opt/sadpanda && \
	source /opt/sadpanda/bin/activate && \
	pip3 install pycrypto python-snappy pytest && \
  # TODO: the below command breaks the build.
	pip3 install /opt/sadpanda/. && \
	chmod +x /opt/sadpanda/sadpanda/bin/sadpanda && \
	chmod +x /opt/sadpanda/sadpanda/bin/sadpanda-shell

# RUN pytest /opt/sadpanda/sadpanda_test

ENV PATH "$PATH:/opt/sadpanda/sadpanda/bin"

#ENTRYPOINT ["sadpanda --config-file /opt/sadpanda/sadpanda/conf/sadpanda.yml"] # --keyfile /opt/sadpanda/sadpanda/blockchain.evk --datastore /opt/sadpanda/sadpanda/data/blockchain.ev"]
