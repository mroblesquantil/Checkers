def flatten_list(list_of_lists, remove_duplicates=False):
	list_ = sum(list_of_lists, [])
	if remove_duplicates:
		list_ = rm_duplicates(list_)
	return list_


def rm_duplicates(list_):
	# Todo: Implement this method
	return list_


