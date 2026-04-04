DROP PROCEDURE IF EXISTS upsert_contact(VARCHAR, VARCHAR, VARCHAR);
DROP PROCEDURE IF EXISTS delete_contact(TEXT);
DROP PROCEDURE IF EXISTS insert_many_contacts(TEXT[]);

CREATE OR REPLACE PROCEDURE upsert_contact(
    p_firstname VARCHAR,
    p_secondname VARCHAR,
    p_phonenumber VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM phonebook
        WHERE firstname = p_firstname AND secondname = p_secondname
    ) THEN
        UPDATE phonebook
        SET phonenumber = p_phonenumber
        WHERE firstname = p_firstname AND secondname = p_secondname;
    ELSE
        INSERT INTO phonebook (firstname, secondname, phonenumber)
        VALUES (p_firstname, p_secondname, p_phonenumber);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_contact(p_value TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE firstname ILIKE p_value
       OR secondname ILIKE p_value
       OR phonenumber = p_value;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_many_contacts(p_contacts TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    item TEXT;
    parts TEXT[];
    f_name VARCHAR;
    s_name VARCHAR;
    phone VARCHAR;
BEGIN
    FOREACH item IN ARRAY p_contacts LOOP
        parts := string_to_array(item, ',');
        IF array_length(parts, 1) != 3 THEN
            RAISE NOTICE 'INVALID: Wrong format (%)', item;
            CONTINUE;
        END IF;

        f_name := trim(parts[1]);
        s_name := trim(parts[2]);
        phone := trim(parts[3]);

        IF phone !~ '^(\+7|8)7[0-9]{9}$' THEN
            RAISE NOTICE 'INVALID: Wrong phone format (%)', phone;
            CONTINUE;
        END IF;

        INSERT INTO phonebook (firstname, secondname, phonenumber)
        VALUES (f_name, s_name, phone);
    END LOOP;
END;
$$;