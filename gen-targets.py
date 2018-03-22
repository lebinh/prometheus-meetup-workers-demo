import json

origins = {
    'dgo': 'https://lebinh.sgp1.digitaloceanspaces.com',
    'aws': 'https://lebinh.s3-ap-southeast-1.amazonaws.com',
    'gcp': 'https://lebinh.storage.googleapis.com'
}

regions = {
    'apac': ['sin', 'hkg', 'nrt', 'tpe', 'maa'],
    'eur': ['lhr', 'txl', 'ams'],
    'afr': ['cai', 'cpt'],
    'nam': ['lax', 'ord'],
    'sam': ['gru', 'eze'],
    'oc': ['syd', 'mel'],
}

files = {
    '1024': 'srandom.txt',
    '102400': 'random.txt',
}


def main():
    res = []
    for region, colos in regions.items():
        for colo in colos:
            for origin, base_url in origins.items():
                for size, filename in files.items():
                    res.append({
                        'targets': ['localhost:8000'],
                        'labels': {
                            'region': region,
                            'colo': colo,
                            'origin': origin,
                            'size_bytes': size,
                            'origin_url': '{}/{}'.format(base_url, filename),
                        }
                    })
    print(json.dumps(res, indent=2))


if __name__ == '__main__':
    main()
