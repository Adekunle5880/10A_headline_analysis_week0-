import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="your_database",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)
cur = conn.cursor()

# Define SQL queries to create tables
create_table_query = """
CREATE TABLE IF NOT EXISTS news_articles (
    article_id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    published_at TIMESTAMP
);
"""

# Execute SQL queries to create tables
cur.execute(create_table_query)
conn.commit()

# Define SQL query to create domains_location table
create_domains_table_query = """
CREATE TABLE IF NOT EXISTS domains_location (
    source_common_name VARCHAR(255) PRIMARY KEY,
    location VARCHAR(255),
    country VARCHAR(255)
);
"""

# Execute SQL query to create domains_location table
cur.execute(create_domains_table_query)
conn.commit()

# Define SQL query to create traffic_data table
create_traffic_table_query = """
CREATE TABLE IF NOT EXISTS traffic_data (
    global_rank INTEGER,
    tld_rank INTEGER,
    domain VARCHAR(255),
    tld VARCHAR(10),
    ref_subnets INTEGER,
    ref_ips INTEGER,
    idn_domain VARCHAR(255),
    idn_tld VARCHAR(10),
    prev_global_rank INTEGER,
    prev_tld_rank INTEGER,
    prev_ref_subnets INTEGER,
    prev_ref_ips INTEGER
);
"""

# Execute SQL query to create traffic_data table
cur.execute(create_traffic_table_query)
conn.commit()

# Load relevant features into the database
# Example: Inserting news articles data
insert_query = """
INSERT INTO news_articles (title, content, published_at)
VALUES (%s, %s, %s);
"""
# Sample data to be inserted
sample_data = [("Title 1", "Content 1", "2024-04-11 12:00:00"),
               ("Title 2", "Content 2", "2024-04-11 13:00:00")]

# Execute SQL queries to insert data
cur.executemany(insert_query, sample_data)
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
