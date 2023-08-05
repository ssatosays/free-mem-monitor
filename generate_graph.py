import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv('output.csv')

    def get_suffix(first_free_mem):
        suffixes = ['B', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi']
        for s in suffixes:
            if first_free_mem.endswith(s):
                return s
        return None

    suffix = get_suffix(df['free-mem'][0])
    if suffix is None:
        raise ValueError(
            "Invalid free memory format. "
            "Expected suffixes are: 'B', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi'"
        )

    df['free-mem'] = df['free-mem'].apply(lambda x: float(x.rstrip(suffix)))
    df['date'] = pd.to_datetime(df['date'])

    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['free-mem'])
    max_index, max_color = df['free-mem'].idxmax(), 'red'
    min_index, min_color = df['free-mem'].idxmin(), 'blue'
    plt.text(
        df['date'][max_index],
        df['free-mem'][max_index],
        df['free-mem'][max_index],
        color=max_color
    )
    plt.text(
        df['date'][min_index],
        df['free-mem'][min_index],
        df['free-mem'][min_index],
        color=min_color
    )
    plt.title('Free memory transition')
    plt.xlabel('Time')
    plt.ylabel(f'Free memory ({suffix})')
    plt.savefig('free_memory_transition.png')


if __name__ == '__main__':
    main()
