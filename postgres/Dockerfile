FROM postgres:alpine
COPY setup.sql /docker-entrypoint-initdb.d/setup.sql
ADD setup.sql /docker-entrypoint-initdb.d/setup.sql
COPY insert.sql /docker-entrypoint-initdb.d/insert.sql
ADD insert.sql /docker-entrypoint-initdb.d/insert.sql
RUN chmod a+r /docker-entrypoint-initdb.d/setup.sql
RUN chmod a+r /docker-entrypoint-initdb.d/insert.sql
