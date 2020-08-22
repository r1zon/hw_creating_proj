import csv

from django.shortcuts import render

from table.models import Table, Savepath


def table_view(request):
    table_params = Table.objects.last()
    CSV_FILENAME = Savepath.objects.first().field_name
    if table_params is not None:
        COLUMNS = [
            {'name': ('id', table_params.id_name,),
             'width': table_params.id_width,
             'num': table_params.id_num},
            {'name': ('name', table_params.name_name,),
             'width': table_params.name_width,
             'num': table_params.name_num},
            {'name': ('price', table_params.price_name,),
             'width': table_params.price_width,
             'num': table_params.price_num},
            {'name': ('release_date', table_params.release_date_name,),
             'width': table_params.release_date_width,
             'num': table_params.release_num},
            {'name': ('lte_exists', table_params.lte_exists_name,),
             'width': table_params.lte_exists_width,
             'num': table_params.lte_num},
        ]
    template = 'table.html'
    with open(CSV_FILENAME, 'rt') as csv_file:
        header = []
        table = []
        table_reader = csv.reader(csv_file, delimiter=';')
        for table_row in table_reader:
            if not header:
                header = {idx: value for idx, value in enumerate(table_row)}
            else:
                row = {header.get(idx) or 'col{:03d}'.format(idx): value
                       for idx, value in enumerate(table_row)}
                table.append(row)

        context = {
            'columns': sorted(COLUMNS, key=lambda x: x['num']),
            'table': table,
            'csv_file': CSV_FILENAME
        }
        result = render(request, template, context)
    return result
