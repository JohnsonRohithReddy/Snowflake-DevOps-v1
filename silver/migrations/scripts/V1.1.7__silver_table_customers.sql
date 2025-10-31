CREATE SCHEMA IF NOT EXISTS {{ sf_schema }};
CREATE OR REPLACE TABLE {{ database_name }}.{{ sf_schema }}.Customer_table_silver
(
    Customer_ID VARCHAR,
    Customer_Name VARCHAR,
    SALE_DATE DATE,
    QUANTITY INT,
    UNIT_PRICE FLOAT,
    STORE_ID VARCHAR,
    _INSERTED_TIMESTAMP TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);
