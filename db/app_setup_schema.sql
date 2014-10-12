-- App Setup Database Schema
-- App Setup will store the application setup information for apps connected to DocuDB

\connect appsetup;

CREATE TABLE app (
  name              VARCHAR(60) UNIQUE NOT NULL,
  key               UUID UNIQUE NOT NULL,
  private_key       UUID UNIQUE NOT NULL,
  settings          JSONB,
  PRIMARY KEY(key)
);

CREATE TABLE app_group (
  id                    SERIAL,
  app_key               UUID REFERENCES app (key),
  name                  VARCHAR(60) UNIQUE NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE app_user (
  id                    SERIAL,
  username              VARCHAR(60) UNIQUE NOT NULL,
  email                 VARCHAR(250) UNIQUE NOT NULL,
  "passowrd"            CHAR(256),
  details               JSONB,
  PRIMARY KEY(id)
);


CREATE TABLE group_user (
  group_id              INTEGER REFERENCES app_group (id),
  user_id               INTEGER REFERENCES app_user (id)
);

CREATE TABLE permission (
  id                    SERIAL,
  name                  VARCHAR(30),
  PRIMARY KEY(id)
);

CREATE TABLE group_permission (
  group_id              INTEGER REFERENCES app_group (id),
  permission_id         INTEGER REFERENCES permission (id)
);