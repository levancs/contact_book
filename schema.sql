CREATE TABLE contacts (
    contact_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE phone_numbers (
    phone_id SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES contacts(contact_id) ON DELETE CASCADE,
    number TEXT NOT NULL,
    type TEXT NOT NULL,
    UNIQUE(contact_id, number)
);

CREATE TABLE tags (
    tag_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE contact_tags (
    contact_id INTEGER REFERENCES contacts(contact_id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(tag_id) ON DELETE CASCADE,
    PRIMARY KEY (contact_id, tag_id)
);