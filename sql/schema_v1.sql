-- -- -- -- -- --
-- GUILD: ID, OWNER_ID, _NAME
-- USER: ID, _NAME
-- -- -- -- -- -- 


CREATE TABLE IF NOT EXISTS guilds (
  id bigint unsigned NOT NULL,
  owner_id bigint unsigned NOT NULL
  _name text NOT NULL

  PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS users (
  id bigint unsigned NOT NULL,
  _name text NOT NULL
  -- TODO: discriminator
  PRIMARY KEY (id)
);


-- -- -- -- -- --
-- CHANNELS: GUILD_ID, ID, _NAME
-- MESSAGES: PARENT_ID, ID, CONTENT, SENT_AT 
-- -- -- -- -- -- 

CREATE TABLE IF NOT EXISTS channels (
  guild_id bigint unsigned NOT NULL,
  id bigint unsigned NOT NULL,
  _name text NOT NULL

  PRIMARY KEY (guild_id),
  FOREIGN KEY (guild_id) REFERENCES guilds(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS messages (
  parent_id bigint unsigned NOT NULL, -- This could be either a USER or a CHANNEL
  id bigint unsigned NOT NULL
  content text NOT NULL,
  sent_at DATETIME NOT NULL,

  PRIMARY KEY (parent_id),
);

