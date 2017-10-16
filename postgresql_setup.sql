SELECT pg_terminate_backend(pg_stat_activity.pid)
  FROM pg_stat_activity
  WHERE pg_stat_activity.datname = 'gyfted_dev'
    AND pid <> pg_backend_pid();

DROP DATABASE gyfted_dev;

CREATE DATABASE gyfted_dev;

\q

-- run with:
-- psql -a -f postgresql_setup.sql


-- then run:
-- python3 db_create.py


-- finally run
-- psql -a -f postgresql_view.sql


-- or use
-- make recreatedb
