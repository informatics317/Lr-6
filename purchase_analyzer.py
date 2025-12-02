def read_purchases(path):
    purchases = []
    with open(path, 'r',  encoding='utf-8') as f:
        for string in f:
            string = string.strip()
            if not string:
                continue
            part = string.split(';')
            if len(part) != 5:
                continue
            try:
                price = float(part[3])
                qty = int(part[4])
                if price < 0 or qty < 0:
                    continue
                purchases.append({'date': part[0],
                                  'category': part[1],
                                  'name': part[2],
                                  'price': price,
                                  'qty': qty})
            except:
                ...
    return purchases


def saving_errors(path):
    bad = []
    with open(path, 'r', encoding='utf-8') as f:
        for string in f:
            original = string.strip()
            if not original:
                bad.append(original)
                continue
            part = original.split(';')
            if len(part) != 5:
                bad.append(original)
            try:
                price = float(part[3])
                qty = int(part[4])
                if price < 0 or qty < 0:
                    bad.append(original)
            except:
                bad.append(original)
    return bad


def count_errors(path):
    errors = 0
    with open(path, 'r',  encoding='utf-8') as f:
        for string in f:
            string = string.strip()
            if not string:
                errors += 1
                continue
            parts = string.split(';')
            if len(parts) != 5:
                errors += 1
                continue
            try:
                price = float(parts[3])
                qty = int(parts[4])
                if price < 0 or qty < 0:
                    errors += 1
            except:
                errors += 1
    return errors


def total_spent(purchases):
    return sum(s['price'] * s['qty'] for s in purchases)


def spent_by_category(purchases):
    categories = {}
    for s in purchases:
        category = s['category']
        total = s['price'] * s['qty']
        if category in categories:
            categories[category] += total
        else:
            categories[category] = total
    return categories


def total(purchase):
    return purchase['price'] * purchase['qty']

def top_n_expensive(purchases, n=3):
    sorted_purchases = sorted(purchases, key=total, reverse=1)
    return sorted_purchases[:n]


def write_report(purchases, errors, out_path):
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('Отчет\n')
        f.write(f'Кол-во валидных строк: {len(purchases)}\n')
        f.write(f'Кол-во ошибок: {errors}\n')
        f.write(f'Общая сумма: {total_spent(purchases)}\n')
        f.write('Суммы по категориям:\n')
        categories = spent_by_category(purchases)
        for category in categories:
            f.write(f'   {category}: {categories[category]}\n')
        f.write('Топ-3 покупок по стоимости:\n')
        for s in top_n_expensive(purchases, 3):
            total = s['price'] * s['qty']
            f.write(f'  {s['date']} {s['category']} {s['name']} {total}\n')





