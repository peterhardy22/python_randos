import logging


def main() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%m-%d-%Y %H:%M:%S",
        filename="randos_part_2/basic.log"
    )

    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")


if __name__ == "__main__":
    main()

    numbers_list: list = [1, 2, 3, 4, 5]
    for item in numbers_list:
        if item == 3:
            logging.critical(item)

        if item % 2 == 0:
            logging.info(item)
        
        if item % 2 != 0 and item != 3:
            logging.error(item)

    