import pandas as pd
import numpy as np
from datetime import datetime


if __name__ == "__main__":
    positions_ = np.random.choice([-1, 1, 0, 0.25, -0.25, 0.5, -0.5, -0.75, 0.75], size=(24, ))

    df = pd.DataFrame(data={
        "datetime": list(pd.date_range(start=datetime(2023, 8, 23, 0), end=datetime(2023, 8, 23, 23, 0), freq="1H")),
        "fix1": positions_,
        "fix2": -positions_
    })

    df.to_csv("sample_positions_file.csv", index=False)

