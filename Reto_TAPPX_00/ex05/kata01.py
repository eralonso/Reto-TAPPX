kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

print("%s" % "\n".join(("".join((" was created by ".join(str(kata)[1:-1:].split(': '))).split("'"))).split(", ")))
