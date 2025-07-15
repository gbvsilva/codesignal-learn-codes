class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child is not child_node]

# Define a Company Hierarchy as a Non-Binary Tree
company_hierarchy_root = TreeNode("CEO")

vp_marketing = TreeNode("VP Marketing")
vp_finance = TreeNode("VP Finance")
vp_engineering = TreeNode("VP Engineering")

company_hierarchy_root.add_child(vp_marketing)
company_hierarchy_root.add_child(vp_finance)
company_hierarchy_root.add_child(vp_engineering)

# Let's add some more
director_marketing = TreeNode("Director Marketing")
vp_marketing.add_child(director_marketing)

engineer = TreeNode("Engineer")
senior_engineer = TreeNode("Senior Engineer")
product_manager = TreeNode("Product Manager")
vp_engineering.add_child(senior_engineer)
vp_engineering.add_child(product_manager)
senior_engineer.add_child(engineer)

# Function to print the Company Hierarchy Tree (i.e., Pre-order traversal)
def print_company_hierarchy(node):
    if node is None:
        return
    else:
        print(f'Position -> {node.value}')
        for child in node.children:
            print_company_hierarchy(child)

# Print the company hierarchy
print_company_hierarchy(company_hierarchy_root)
