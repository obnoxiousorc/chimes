def import_notes(lines):
    result = []
    for line in lines:
        parts = line.strip().split(' ')
        result.append(
            {
                'notes': parts[:-1],
                'duration': float(parts[-1])
            })
    return result


def export_notes(song):
    result = ''
    for time_slot in song:
        result += ' '.join(time_slot['notes']) + f" {time_slot['duration']}\n"
    return result
