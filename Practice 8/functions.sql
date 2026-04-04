DROP FUNCTION IF EXISTS search_contacts(TEXT);
DROP FUNCTION IF EXISTS get_contacts_paginated(INT, INT);

CREATE OR REPLACE FUNCTION search_contacts(p_pattern TEXT)
RETURNS TABLE(id INT, firstname VARCHAR, secondname VARCHAR, phonenumber VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT pb.id, pb.firstname, pb.secondname, pb.phonenumber
    FROM phonebook pb
    WHERE pb.firstname ILIKE '%' || p_pattern || '%'
       OR pb.secondname ILIKE '%' || p_pattern || '%'
       OR pb.phonenumber ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, firstname VARCHAR, secondname VARCHAR, phonenumber VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT pb.id, pb.firstname, pb.secondname, pb.phonenumber
    FROM phonebook pb
    ORDER BY pb.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;