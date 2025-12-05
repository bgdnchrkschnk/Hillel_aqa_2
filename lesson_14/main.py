from custom_file_logger import logger


succesful_transactions = []

def get_completed_transactions(transactions_l: list) -> None:
    logger.debug("Stating to process transactions")
    for transaction in transactions_l:
        logger.debug(f"Checking transaction with id={transaction["id"]}")
        if transaction['status'] == 'completed':
            logger.info(f"Transaction with id={transaction['id']} completed. Adding to succesful transactions")
            succesful_transactions.append(transaction)
        else:
            logger.info(f"Transaction with id={transaction['id']} not completed. Waiting for approval..")




transactions = [
    {"id": 2536, "status": "pending"},
    {"id": 2537, "status": "completed"},
    {"id": 2538, "status": "pending"},
    {"id": 2539, "status": "rejected"},
]


get_completed_transactions(transactions)