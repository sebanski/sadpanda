FROM centos
MAINTAINER alex.balzer <zabbal22@gmail.com>

# TODO: debug this container

COPY . /opt/sadpanda/

COPY keygen.py /etc/sadpanda.d/keygen.py
RUN /usr/bin/python /etc/sadpanda.d/keygen.py --num-chars=257654 >> /etc/sadpanda.d/poppyfarms.ve && \
	/usr/bin/python /etc/sadpanda.d/keygen.py --num-chars=257654 >> /opt/sadpanda/sadpanda/blockchain.evk && \
	yum -y install epel-release && \
	yum -y install python-pip libsnappy && \
	pip install virtualenv && \
	virtualenv /opt/sadpanda/ && \
	source /opt/sadpanda/bin/activate && \
	pip install pycrypto python-snappy && \
	pip install /opt/sadpanda/. && \
	chmod +x /opt/sadpanda/sadpanda/bin/sadpanda && \
	chmod +x /opt/sadpanda/sadpanda/bin/sadpanda-shell

ENV PATH=$PATH:/opt/sadpanda/sadpanda/bin

ENTRYPOINT ["sadpanda --config-file /opt/sadpanda/sadpanda/conf/sadpanda.yml"] # --keyfile /opt/sadpanda/sadpanda/blockchain.evk --datastore /opt/sadpanda/sadpanda/data/blockchain.ev"]
