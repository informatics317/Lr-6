from purchase_analyzer import*

def test_read_purchases():
    purchases = read_purchases('test_file.txt')
    assert len(purchases) == 5
    assert purchases[0]['name'] == 'Apple'
    assert purchases[1]['price'] == 1000
    assert purchases[2]['category'] == 'food'
    assert purchases[3]['qty'] == 2


def test_saving_errors():
    errors = saving_errors('test_file.txt')
    assert errors == ['2025-10-01;clothes;Shoes;30;extra',
                      '',
                      '2025-10-02;other;Pen;0.60;5.6',
                      '2025-10-04;home;Bed;1.90;',
                      '',
                      '2023-10-05;food;Milk;1.0;-3',
                      '2025-10-06;transport;Taxi;ten;1']


def test_count_errors():
    assert count_errors('test_file.txt') == 7

def test_total_spent():
    purchases = read_purchases('test_file.txt')
    assert total_spent(purchases) == 1062.3

def test_spent_by_category():
    purchases = read_purchases('test_file.txt')
    spend = spent_by_category(purchases)
    assert spend['food'] == 12.3
    assert spend['other'] == 1000

def test_top_n_expensive():
    purchases = read_purchases('test_file.txt')
    top = top_n_expensive(purchases, n = 3)
    assert top[0]['category'] == 'other'
    assert top[1]['price'] * top[1]['qty'] == 50
    assert top[2]['name'] == 'Bread'
















