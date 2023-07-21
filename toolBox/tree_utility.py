from PySide6.QtWidgets import QTreeWidgetItem, QTreeWidget


def get_subtree_nodes(tree_widget_item: QTreeWidgetItem) -> list[QTreeWidgetItem]:
    """returns all the widgets in the suptree rooted at the biven node"""
    nodes = [tree_widget_item]
    for i in range(tree_widget_item.childCount()):
        nodes.extend(get_subtree_nodes(tree_widget_item.child(i)))
    return nodes

def get_all_items(treeWidget: QTreeWidget) -> list[QTreeWidgetItem]:
    """returns all QTreeWidgets in the given treeWidget"""
    all_items = []
    for i in range(treeWidget.topLevelItemCount()):
        top_item = treeWidget.topLevelItem(i)
        all_items.extend(get_subtree_nodes(top_item))
    return all_items
