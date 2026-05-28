"""
We are developing a stock trading data management software that tracks the prices of different stocks over time and provides useful statistics.

The program includes three classes: `Stock`, `PriceRecord`, and `StockCollection`.

Classes:
* The `Stock` class represents data about a specific stock.
* The `PriceRecord` class holds information about a single price record for a stock.
* The `StockCollection` class manages a collection of price records for a particular stock and provides methods to retrieve useful statistics about the stock's prices.

To begin with, we present you with two tasks:
1-1) Read through and understand the code below. Please take as much time as necessary, and feel free to run the code.
1-2) The test for StockCollection is not passing due to a bug in the code. Make the necessary changes to StockCollection to fix the bug.
"""

import unittest


class Stock:
    """ Data about a particular stock. """

    def __init__(self, symbol, name):
        self.symbol = symbol  # String, the symbol of the stock
        self.name = name  # String, the name of the stock

    def __eq__(self, other):
        if not isinstance(other, self.__class__): return False
        return (self.symbol == other.symbol and self.name == other.name)


class PriceRecord:
    """Data and methods about a single price record of a stock."""

    def __init__(self, stock, price, date):
        self.stock = stock  # a Stock object representing the stock
        self.price = price  # int, the price of the stock
        self.date = date  # str, the date of the price record is of the format "YYYY-MM-DD"

    def __eq__(self, other):
        if not isinstance(other, self.__class__): return False
        return (self.stock == other.stock and self.price == other.price and self.date == other.date)


class StockCollection(object):
    """
        Data for a collection of price records for a particular stock, and methods for getting
        useful statistics about the stock's prices.
    """

    def __init__(self, stock):
        self.price_records = []  # list of PriceRecord objects, the price records for this particular stock
        self.stock = stock  # stock, the Stock this StockCollection is for

    def get_num_price_records(self):
        """Returns the number of PriceRecords in this StockCollection"""
        return len(self.price_records)

    def add_price_record(self, price_record):
        """Adds a PriceRecord to this StockCollection."""
        if price_record.stock != self.stock:
            raise ValueError("PriceRecord's Stock is not the same as the StockCollection's")
        self.price_records.append(price_record)
        print(self.price_records)

    def get_max_price(self):
        """Return the maximum price recorded in this StockCollection."""
        if len(self.price_records) == 0:
            return None
        else:
            return max(price_record.price for price_record in self.price_records)

    def get_min_price(self):
        """Return the minimum price recorded in this StockCollection."""
        if len(self.price_records) == 0:
            return None
        return min(price_record.price for price_record in self.price_records)

    def get_avg_price(self):
        """Return the average price recorded in this StockCollection."""
        total = sum(price_record.price for price_record in self.price_records)
        count = len(self.price_records)
        if count != 0:
            return total / count
        else:
            return None


class TestSuite(unittest.TestCase):
    def test_price_record(self):
        """Test basic PriceRecord functionality"""
        test_stock = Stock("AAPL", "Apple Inc.")
        test_price_record = PriceRecord(test_stock, 100, "2023-07-01")
        self.assertEqual(test_price_record.stock, test_stock)
        self.assertEqual(test_price_record.price, 100)
        self.assertEqual(test_price_record.date, "2023-07-01")

    def make_stock_collection(self, stock, price_data):
        """
            Create a new StockCollection for test purposes.

            stock: The Stock object this StockCollection is for
            price_data: a list of tuples. Each tuple represents a price record for
                        a single date.
        """
        stock_collection = StockCollection(stock)
        for price_record_data in price_data:
            price_record = PriceRecord(stock, price_record_data[0], price_record_data[1])
            stock_collection.add_price_record(price_record)
        return stock_collection

    def test_stock_collection(self):
        """Test basic StockCollection functionality"""

        test_stock = Stock("AAPL", "Apple Inc.")
        stock_collection = StockCollection(test_stock)
        self.assertEqual(stock_collection.get_num_price_records(), 0)
        self.assertEqual(stock_collection.get_max_price(), None)
        self.assertEqual(stock_collection.get_min_price(), None)
        self.assertEqual(stock_collection.get_avg_price(), None)

        """
        Price Records:
        Price:  110         112         90          105
        Date:   2023-06-29  2023-07-01  2023-06-28  2023-07-06
        """
        price_data = [
            (110, "2023-06-29"),
            (112, "2023-07-01"),
            (90, "2023-06-28"),
            (105, "2023-07-06")
        ]
        test_stock = Stock("AAPL", "Apple Inc.")
        stock_collection = self.make_stock_collection(test_stock, price_data)
        self.assertEqual(stock_collection.get_num_price_records(), len(price_data))
        self.assertEqual(stock_collection.get_max_price(), 112)
        self.assertEqual(stock_collection.get_min_price(), 90)
        self.assertAlmostEqual(stock_collection.get_avg_price(), 104.25, 1)


if __name__ == '__main__':
    unittest.main()
