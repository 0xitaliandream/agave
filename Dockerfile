FROM anzaxyz/agave:v2.2.14

COPY agave-validator /usr/bin/agave-validator

RUN chmod +x /usr/bin/agave-validator

EXPOSE 9000