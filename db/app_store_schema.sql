-- App Store Database Schema

CREATE DATABASE appstore;
\connect appstore;

CREATE TABLE appkey_doc (
  doc_id                  BIGSERIAL,
  doc_path                VARCHAR(350) UNIQUE NOT NULL,
  parent_path             VARCHAR(350) UNIQUE NOT NULL,
  doc                     JSONB,
  doc_version             INTEGER,
  status                  VARCHAR(10),
  create_dt               TIMESTAMPTZ,
  update_dt               TIMESTAMPTZ,
  create_user             INTEGER, -- We do not enforce FK constraint here
  PRIMARY KEY(doc_id)
);

CREATE INDEX ON appkey_doc(doc_path);
CREATE INDEX ON appkey_doc(parent_path);
CREATE INDEX ON appkey_doc(status);

CREATE TABLE appkey_users (
  user_id                 SERIAL,
  username                VARCHAR(60),
  email                   VARCHAR(250),
  first_name              VARCHAR(60),
  last_name               VARCHAR(60),
  "password"              CHAR(250),
  PRIMARY KEY(user_id)
);

CREATE INDEX ON appkey_users(username);
CREATE INDEX ON appkey_users(email);


CREATE TABLE appkey_groups (
  group_id                SERIAL,
  group_name              VARCHAR(60),
  doc_path                VARCHAR(350),
  inc_deps                BOOLEAN,
  read_permission         BOOLEAN,
  write_permission        BOOLEAN,
  delete_permission       BOOLEAN,
  PRIMARY KEY(group_id)
);

CREATE INDEX ON appkey_groups(group_name);
CREATE INDEX ON appkey_groups(doc_path);

CREATE TABLE appkey_group_users (
  group_id                INTEGER REFERENCES appkey_groups (group_id),
  user_id                 INTEGER REFERENCES appkey_users  (user_id)
);

CREATE TABLE appkey_workflow (
  wf_id                   SERIAL,
  wf_name                 VARCHAR(60),
  create_dt               TIMESTAMPTZ,
  update_dt               TIMESTAMPTZ,
  create_user             INTEGER, -- We do not enforce FK constraint here
  PRIMARY KEY(wf_id)
);

CREATE INDEX ON appkey_workflow(wf_name);

CREATE TABLE appkey_stage (
  stage_id                SERIAL,
  wf_id                   INTEGER REFERENCES appkey_workflow (wf_id),
  stage_name              VARCHAR(60),
  status                  VARCHAR(10),
  stage_order             INTEGER,
  meta                    JSONB,
  PRIMARY KEY(stage_id)
);

CREATE INDEX ON appkey_stage(stage_name);
CREATE INDEX ON appkey_stage(status);

CREATE TABLE appkey_stage_doc (
  doc_id                  BIGINT REFERENCES appkey_doc(doc_id),
  stage_id                INTEGER REFERENCES appkey_stage(stage_id),
  status                  VARCHAR(60),
  meta                    JSONB
);

CREATE TABLE appkey_schema  (
  schema_name             VARCHAR(60),
  schema_value            JSONB
);

CREATE INDEX ON appkey_schema(schema_name);