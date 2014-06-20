-- App Setup Database Schema
-- Part of the DocuDB project.  App Setup will store the application setup information for apps
-- connected to DocuDB
DROP DATABASE IF EXISTS appsetup;
CREATE DATABASE appsetup;
\connect appsetup;

CREATE TABLE app (
  app_name              VARCHAR(60) UNIQUE NOT NULL,
  app_key               UUID UNIQUE NOT NULL,
  private_key           UUID UNIQUE NOT NULL,
  PRIMARY KEY(app_key)
);

CREATE TABLE app_setings (
  app_key               UUID REFERENCES app (app_key),
  settings              JSONB
);

CREATE TABLE app_user (
  user_id               SERIAL,
  app_key               UUID REFERENCES app (app_key),
  username              VARCHAR(60) UNIQUE NOT NULL,
  email                 VARCHAR(250) UNIQUE NOT NULL,
  "passowrd"            CHAR(256),
  PRIMARY KEY(user_id)

);

CREATE TABLE user_details (
  user_id               INTEGER REFERENCES app_user (user_id),
  details               JSONB
);

CREATE TABLE app_group (
  group_id              SERIAL,
  app_key               UUID REFERENCES app (app_key),
  group_name            VARCHAR(60) UNIQUE NOT NULL,
  read_permission       BOOLEAN,
  write_permission      BOOLEAN,
  PRIMARY KEY(group_id)
);

CREATE TABLE group_user (
  group_id              INTEGER REFERENCES app_group (group_id),
  user_id               INTEGER REFERENCES app_user (user_id)
);
