print('\nData ini dikirimkan oleh server Gojek, untuk memberikan informasi driver disekitar pemakai aplikasi')
data_dari_serve_gojek = {
    'tanggal' : '2020-06-10',
    'driver_list' : [
        {'nama': 'arief', 'jarak' : 10},
        {'nama': 'arenta', 'jarak' : 20},
        {'nama': 'naldo',  'jarak' : 30},
        {'nama': 'haikal', 'jarak' : 50},

    ]
}

print(data_dari_serve_gojek)
print(f"\nDriver disekitar sini{data_dari_serve_gojek['driver_list']}")
print(f"Driver #1 {data_dari_serve_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_serve_gojek['driver_list'][3]}")
print(f"Driver terdekat berjarak {data_dari_serve_gojek['driver_list'][0]['jarak']}meter")