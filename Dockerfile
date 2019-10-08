FROM python
ENV STRAYTORCH_HOME /opt/straytorch
COPY bin $STRAYTORCH_HOME/bin
COPY files $STRAYTORCH_HOME/files
COPY reports $STRAYTORCH_HOME/reports
COPY templates $STRAYTORCH_HOME/templates
COPY straytorch.py $STRAYTORCH_HOME/
ENV PATH $PATH:$STRAYTORCH_HOME/bin
RUN pip install pyyaml