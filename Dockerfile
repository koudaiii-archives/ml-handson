FROM ubuntu:14.04
RUN echo "nameserver 172.17.42.1" > /etc/resolv.conf
RUN echo "nameserver 8.8.8.8" >> /etc/resolv.conf
RUN apt-get update
RUN apt-get install -y git gcc make openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl
RUN cd /usr/local/
RUN git clone git://github.com/yyuu/pyenv.git ./pyenv
RUN mkdir -p ./pyenv/versions ./pyenv/shims
RUN　cd /usr/local/pyenv/plugins/
RUN　git clone git://github.com/yyuu/pyenv-virtualenv.git
RUN echo 'export PYENV_ROOT="/usr/local/pyenv"' | sudo tee -a /etc/profile.d/pyenv.sh
RUN echo 'export PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}"' | sudo tee -a /etc/profile.d/pyenv.sh
CMD ['source', '/etc/profile.d/pyenv.sh']
CMD ['pyenv', 'install', 'miniconda3-3.8.3']
CMD ['pyenv', 'rehash']
CMD ['pyenv', 'global', 'miniconda3-3.8.3']
RUN wget -qO- https://bootstrap.pypa.io/get-pip.py | python
RUN　yes | pip install virtualenv
RUN　conda create -n ml_env numpy scipy scikit-learn matplotlib cython ipython ipython-notebook
RUN source /usr/local/pyenv/versions/miniconda3-3.8.3/envs/ml_env/bin/activate ml_env
RUN apt-get install -y build-essential gfortran libgfortran3 python3-dev libblas-dev libatlas-base-dev cython
RUN apt-get autoremove -y
RUN apt-get clean all
