class DepartmentTree:
    def __init__(self, name):
        self.name = name
        self.subdepartments = []

    def add_subdepartment(self, subdept_name):
        self.subdepartments.append(DepartmentTree(subdept_name))

    def traverse(self, visited=None):
        if visited is None:
            visited = set()
        print(self.name)
        visited.add(self.name)

        # TODO: Add logic here to complete the traversal of the department tree
        for dept in self.subdepartments:
            if dept.name not in visited:
                dept.traverse(visited)

# Build a representation of a company's hierarchy
company_hierarchy = DepartmentTree("CEO")
company_hierarchy.add_subdepartment("CTO")
company_hierarchy.add_subdepartment("CFO")
company_hierarchy.add_subdepartment("COO")

# Expand the CTO's branch
cto_branch = company_hierarchy.subdepartments[0]
cto_branch.add_subdepartment("Infrastructure")
cto_branch.add_subdepartment("App Development")
cto_branch.add_subdepartment("Security")

# Expand the CFO's branch
cfo_branch = company_hierarchy.subdepartments[1]
cfo_branch.add_subdepartment("Accounting")
cfo_branch.add_subdepartment("Investor Relations")

# Now let's do a DFS traversal to print all departments
print("DFS Traversal of Company's Departments:")
company_hierarchy.traverse()
