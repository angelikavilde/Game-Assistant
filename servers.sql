CREATE TABLE servers(
    server_id SMALLINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    server_object BYTEA);