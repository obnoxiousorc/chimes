def import_notes(data):
    lines = data.split('\n')
    result = []
    for line in lines:
        parts = line.strip().split(' ')
        result.append(
            {
                'notes': parts[:-1],
                'delay': float(parts[-1])
            })
    return result


def export_notes(song):
    result = ''
    for time_slot in song:
        result += ' '.join(time_slot['notes']) + f" {time_slot['delay']}\n"
    return result
