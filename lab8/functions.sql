CREATE OR REPLACE FUNCTION search_contacts(p_pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.phone
    FROM contacts c
    WHERE c.name ILIKE '%' || p_pattern || '%'
       OR c.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.phone
    FROM contacts c
    ORDER BY c.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION insert_many_contacts(p_names TEXT[], p_phones TEXT[])
RETURNS TABLE(invalid_name TEXT, invalid_phone TEXT) AS $$
DECLARE
    i INT;
    v_name TEXT;
    v_phone TEXT;
BEGIN
    FOR i IN 1..array_length(p_names, 1) LOOP
        v_name := p_names[i];
        v_phone := p_phones[i];

        IF v_phone ~ '^\+?[0-9]{10,15}$' THEN
            IF EXISTS (SELECT 1 FROM contacts WHERE contacts.name = v_name) THEN
                UPDATE contacts SET phone = v_phone WHERE contacts.name = v_name;
            ELSE
                INSERT INTO contacts(name, phone) VALUES(v_name, v_phone);
            END IF;
        ELSE
            invalid_name := v_name;
            invalid_phone := v_phone;
            RETURN NEXT;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
