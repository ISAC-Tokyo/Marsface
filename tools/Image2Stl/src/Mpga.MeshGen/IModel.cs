using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Mpga.MeshGen
{
    public interface IModel
    {
        Triangle[] ToMesh();
    }
}
