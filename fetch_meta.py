
import json
import os
from internetarchive import search_items, get_item

COLLECTION = 'ote'

print(f'Fetching identifiers for {COLLECTION}')
results = search_items(f'collection:{COLLECTION}')
identifiers = [x['identifier'] for x in results]
print(f'Fetched {len(identifiers)} potential identifiers')

if not os.path.exists('data/meta'):
  os.mkdir('data/meta')

num = 0
for id in identifiers:
  num += 1
  print(f'Fetching metadata for {id} [{num} / {len(identifiers)}]')
  item = get_item(id)
  meta = item.item_metadata
  originals = [x for x in meta['files'] if x['source'] == 'original']
  derivatives = [x for x in meta['files'] if x['source'] == 'derivative']
  print(f'  item has {len(originals)} original files')
  print(f'  item has {len(derivatives)} derivative files')
  original_mp3s = [x for x in originals if 'mp3' in x['format'].lower()]
  derivative_mp3s = [x for x in derivatives if 'mp3' in x['format'].lower()]
  mp3s = original_mp3s + derivative_mp3s
  if len(mp3s) > 0:
    print(f'  {id} has {len(mp3s)} mp3 files')
    out = open(f'data/meta/{id}.json', 'wt')
    out.write(json.dumps(meta, indent=2))
    out.close()
  else:
    print(f'  {id} has no mp3 files, skipping...')
