class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def process_queries(queries):
    result = []
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            if cur_query.number in contacts:
                del contacts[cur_query.number]
        else:
            name = contacts.get(cur_query.number, "not found")
            result.append(name)
    return result


def write_responses(result):
    for r in result:
        print(r)

if __name__ == '__main__':
    queries = read_queries()
    result = process_queries(queries)
    write_responses(result)