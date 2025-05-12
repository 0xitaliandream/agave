FROM anzaxyz/agave:v2.2.14

COPY ./target/release/agave-validator /usr/bin/agave-validator

RUN chmod +x /usr/bin/agave-validator

EXPOSE 9000