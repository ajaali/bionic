-- App Store Database Schema

\connect appstore;

CREATE TABLE appkey_doc (
  id                      BIGSERIAL,
  path                    VARCHAR(350) UNIQUE NOT NULL,
  parent_path             VARCHAR(350) UNIQUE NOT NULL,
  doc                     JSONB,
  doc_version             INTEGER,
  create_dt               TIMESTAMPTZ,
  update_dt               TIMESTAMPTZ,
  create_user             INTEGER, -- We do not enforce FK constraint here
  PRIMARY KEY(id)
);

CREATE INDEX ON appkey_doc(path);
CREATE INDEX ON appkey_doc(parent_path);

CREATE TABLE appkey_users (
  id                      SERIAL,
  username                VARCHAR(60),
  email                   VARCHAR(250),
  "password"              CHAR(250),
  details                 JSONB,
  PRIMARY KEY(id)
);

CREATE INDEX ON appkey_users(username);
CREATE INDEX ON appkey_users(email);


CREATE TABLE appkey_groups (
  id                      SERIAL,
  name                    VARCHAR(60),
  doc_id                  BIGINT,
  doc_path                VARCHAR(350),
  inc_deps                BOOLEAN,
  permission              VARCHAR(10),
  PRIMARY KEY(id)
);

CREATE INDEX ON appkey_groups(name);
CREATE INDEX ON appkey_groups(doc_id);
CREATE INDEX ON appkey_groups(doc_path);

CREATE TABLE appkey_group_users (
  group_id                INTEGER REFERENCES appkey_groups (id),
  user_id                 INTEGER REFERENCES appkey_users  (id)
);

CREATE TABLE appkey_workflow (
  id                   SERIAL,
  name                 VARCHAR(60),
  create_dt            TIMESTAMPTZ,
  update_dt            TIMESTAMPTZ,
  create_user          INTEGER, -- We do not enforce FK constraint here
  PRIMARY KEY(id)
);

CREATE INDEX ON appkey_workflow(name);

CREATE TABLE appkey_stage (
  id                SERIAL,
  wf_id             INTEGER REFERENCES appkey_workflow (id),
  name              VARCHAR(60),
  status            VARCHAR(10),
  stage_order       INTEGER,
  meta              JSONB,
  PRIMARY KEY(id)
);

CREATE INDEX ON appkey_stage(name);
CREATE INDEX ON appkey_stage(status);

CREATE TABLE appkey_stage_doc (
  doc_id                  BIGINT REFERENCES appkey_doc(id),
  stage_id                INTEGER REFERENCES appkey_stage(id),
  status                  VARCHAR(10),
  meta                    JSONB
);

CREATE TABLE appkey_schema  (
  id                      SERIAL,
  name                    VARCHAR(60),
  value                   JSONB
);

CREATE INDEX ON appkey_schema(name);