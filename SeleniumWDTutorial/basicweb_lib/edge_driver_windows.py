from selenium import webdriver
import time

class RunEdgeTests():
    def test_edge(self):
        driver = webdriver.Edge()
        driver.get('https://www.google.com')
        time.sleep(5) 

edge_test = RunEdgeTests()
edge_test.test_edge()