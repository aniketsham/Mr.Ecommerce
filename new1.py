import datetime

from flask import Flask, flash, request, send_file, redirect, render_template, make_response
import json
import hashlib
import mysql.connector
import base64


a = 3
b = datetime.datetime.now()
c = "2"
d = "Aniket"

prev_hash="0000"


transaction = {"Product_id": a, "Date": b, "Transaction_id": c, "Username": d, "last_block_hash": prev_hash}

transaction = str(transaction)
result = hashlib.sha256(transaction.encode()).hexdigest()

prev_hash = result

b = datetime.datetime.now()

transaction2 = {"Product_id": a, "Date": b, "Transaction_id": c, "Username": d, "last_block_hash": prev_hash}
transaction2 = str(transaction2)

result2 = hashlib.sha256(transaction2.encode()).hexdigest()




