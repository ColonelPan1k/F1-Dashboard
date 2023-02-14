FROM mysql:5.7

ADD docker/mysql/init/f1db.sql /docker-entrypoint-initdb.d/

RUN chown -R mysql:mysql /docker-entrypoint-initdb.d/
